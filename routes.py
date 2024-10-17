from flask import render_template, request, redirect, url_for, flash
from db_config import DatabaseConfig
from db_operations import MembershipDB
from math import ceil

db_config = DatabaseConfig()
db = MembershipDB(db_config)

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/member/list')
    def member_list():
        try:
            page = request.args.get('page', 1, type=int)
            members = db.get_all_members(page=page)
            total_members = db.get_total_members()
            total_pages = ceil(total_members / 15)
            return render_template('members/list.html', members=members, page=page, total_pages=total_pages)
        except Exception as e:
            flash('Error retrieving member list.', 'error')
            return redirect(url_for('index'))

    @app.route('/member/register', methods=['GET', 'POST'])
    def register_member():
        if request.method == 'POST':
            code = request.form['code']
            name = request.form['name']
            transport_type = request.form['transport_type']
            
            try:
                db.register_member(code, name, transport_type)
                flash('Member registered successfully!', 'success')
                return redirect(url_for('member_list'))
            except Exception as e:
                flash('Error registering member. Code might be already in use.', 'error')
            
        return render_template('members/register.html')

    @app.route('/attendance/check-in', methods=['GET', 'POST'])
    def check_in():
        if request.method == 'POST':
            member_code = request.form['member_code']
            
            try:
                member = db.get_member_by_code(member_code)
                
                if not member:
                    flash('Member not found!', 'error')
                    return redirect(url_for('check_in'))
                
                if db.check_attendance_cooldown(member.id, app.config['ATTENDANCE_COOLDOWN_MINUTES']):
                    flash('Cannot check in yet. Please wait for the cooldown period.', 'error')
                    return redirect(url_for('check_in'))
                
                db.record_attendance(member.id)
                
                flash('Check-in successful!', 'success')
                return redirect(url_for('index'))
                
            except Exception as e:
                flash(f'Error during check-in: {str(e)}', 'error')
                return redirect(url_for('check_in'))
            
        return render_template('attendance/check_in.html')

    @app.route('/attendance/list')
    def attendance_list():
        try:
            page = request.args.get('page', 1, type=int)
            attendances = db.get_recent_attendances(page=page)
            total_attendances = db.get_total_attendances()
            total_pages = ceil(total_attendances / 15)
            return render_template('attendance/list.html', attendances=attendances, page=page, total_pages=total_pages)
        except Exception as e:
            flash('Error retrieving attendance list.', 'error')
            return redirect(url_for('index'))

    @app.route('/payments/list')
    def payment_list():
        try:
            page = request.args.get('page', 1, type=int)
            payments = db.get_payments(page=page)
            total_payments = db.get_total_payments()
            total_pages = ceil(total_payments / 15)
            return render_template('payments/list.html', payments=payments, page=page, total_pages=total_pages)
        except Exception as e:
            flash('Error retrieving payment list.', 'error')
            return redirect(url_for('index'))