from .. import condition


class TestYkmanInfo:
    def test_ykman_info(self, ykman_cli):
        info = ykman_cli("info").output
        assert "Device type:" in info
        assert "Serial number:" in info
        assert "Firmware version:" in info

    @condition.fips(False)
    def test_ykman_info_does_not_report_fips_for_non_fips_device(self, ykman_cli):
        info = ykman_cli("info", "--check-fips").output
        assert "FIPS" not in info

    @condition.fips(True)
    def test_ykman_info_reports_fips_status(self, ykman_cli):
        info = ykman_cli("info", "--check-fips").output
        assert "FIPS Approved Mode:" in info
        assert "  FIDO U2F:" in info
        assert "  OATH:" in info
        assert "  OTP:" in info
