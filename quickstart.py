""" Quickstart script for InstaPy usage """

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args
from datetime import datetime

if __name__ == "__main__":
    cli_args = parse_cli_args()

    login_id = "2183702117"
    login_psw = "xogns123!"
    dpt_stn = "대전"
    arr_stn = "울산(통도사)"
    # dpt_dt = "20220603"
    #today
    dpt_dt = datetime.today().strftime("%Y%m%d")
    dpt_tm = "18"

    num_trains_to_check = 2
    want_reserve = cli_args.reserve

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, num_trains_to_check, want_reserve)
    srt.run(login_id, login_psw)