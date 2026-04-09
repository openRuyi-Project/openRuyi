# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sg3_utils
Version:        1.48
Release:        %autorelease
Summary:        Utilities for devices that use SCSI command sets
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://sg.danny.cz/sg/sg3_utils.html
VCS:            git:https://github.com/doug-gilbert/sg3_utils
#!RemoteAsset
Source0:        https://sg.danny.cz/sg/p/sg3_utils-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  systemd

# For compatibility
Provides:       %{name}-libs = %{version}-%{release}

%description
Collection of Linux utilities for devices that use the SCSI command set.
Includes utilities to copy data based on "dd" syntax and semantics (called
sg_dd, sgp_dd and sgm_dd); check INQUIRY data and VPD pages (sg_inq); check
mode and log pages (sginfo, sg_modes and sg_logs); spin up and down
disks (sg_start); do self tests (sg_senddiag); and various other functions.
See the README, CHANGELOG and COVERAGE files. Requires the linux kernel 2.4
series or later. In the 2.4 series SCSI generic device names (e.g. /dev/sg0)
must be used. In the 2.6 series other device names may be used as
well (e.g. /dev/sda).

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.

%package        devel
Summary:        Development library and header files for the sg3_utils library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the %{name} library and its header files for
developing applications.

%install -a
install -m 644 doc/rescan-scsi-bus.sh.8 %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/00-scsi-sg3_config.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/40-usb-blacklist.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/54-before-scsi-sg3_id.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/55-scsi-sg3_id.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/58-scsi-sg3_symlink.rules %{buildroot}/%{_udevrulesdir}
install -m 644 scripts/59-fc-wwpn-id.rules %{buildroot}/%{_udevrulesdir}
install -p -m 755 scripts/fc_wwpn_id %{buildroot}%{_udevrulesdir}/..

%files
%license BSD_LICENSE COPYING
%doc AUTHORS COVERAGE CREDITS ChangeLog README README.sg_start
%{_bindir}/scsi_*
%{_bindir}/sg_*
%{_bindir}/rescan-scsi-bus.sh
%{_bindir}/sginfo
%{_bindir}/sgm_dd
%{_bindir}/sgp_dd
%{_mandir}/man8/scsi_*.8*
%{_mandir}/man8/sg_*.8*
%{_mandir}/man8/rescan-scsi-bus.sh.8*
%{_mandir}/man8/sginfo.8*
%{_mandir}/man8/sgm_dd.8*
%{_mandir}/man8/sgp_dd.8*
%{_mandir}/man8/sg3_utils.8*
%{_mandir}/man8/sg3_utils_json.8*
%{_udevrulesdir}/00-scsi-sg3_config.rules
%{_udevrulesdir}/40-usb-blacklist.rules
%{_udevrulesdir}/54-before-scsi-sg3_id.rules
%{_udevrulesdir}/55-scsi-sg3_id.rules
%{_udevrulesdir}/58-scsi-sg3_symlink.rules
%{_udevrulesdir}/59-fc-wwpn-id.rules
%{_udevrulesdir}/../fc_wwpn_id
%{_libdir}/libsgutils2-%{version}.so.*

%files devel
%{_includedir}/scsi/*.h
%{_libdir}/libsgutils2.so

%changelog
%autochangelog
