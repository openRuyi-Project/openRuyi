# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           open-iscsi
Version:        2.1.11
Release:        %autorelease
Summary:        Linux iSCSI Software Initiator
License:        GPL-2.0-or-later
URL:            https://github.com/open-iscsi/open-iscsi
#!RemoteAsset
Source:         https://github.com/open-iscsi/open-iscsi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dc_args="%{optflags} -fno-strict-aliasing -fno-common -DOFFLOAD_BOOT_SUPPORTED"
BuildOption(conf):  -Discsi_sbindir=%{_sbindir}
BuildOption(conf):  -Ddbroot=%{_sharedstatedir}/iscsi
BuildOption(conf):  -Drulesdir=%{_udevrulesdir}
BuildOption(conf):  -Dlockdir=%{_rundir}/lock/iscsi

BuildRequires:  meson >= 0.54.0
BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  flex
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(libisns)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)

%{?systemd_requires}

%description
This is a transport independent implementation of RFC 3720 iSCSI.
This package contains the user-space control plane, including the iscsid
daemon and the iscsiadm management utility.

%package     -n iscsiuio
Summary:        Linux Broadcom NetXtreme II iSCSI server helper
Requires:       logrotate

%description -n iscsiuio
This tool is used in conjunction with Broadcom NetXtreme II Linux drivers
to provide ARP and DHCP functionality for iSCSI offload.

%package        devel
Summary:        Development files for the iSCSI User-level Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the open-iscsi user-level library include files
and development libraries.

%install -a
ln -sf iscsiuio %{buildroot}%{_sbindir}/brcm_iscsiuio
(cd %{buildroot}%{_sysconfdir}; ln -sf iscsi/iscsid.conf iscsid.conf)
touch %{buildroot}%{_sysconfdir}/iscsi/initiatorname.iscsi
mv %{buildroot}%{_sysconfdir}/logrotate.d/iscsiuiolog %{buildroot}%{_sysconfdir}/logrotate.d/iscsiuio

%post
if [ ! -f %{_sysconfdir}/iscsi/initiatorname.iscsi ] ; then
    /sbin/iscsi-gen-initiatorname
fi
%systemd_post iscsi.service iscsid.service iscsid.socket iscsi-init.service

%preun
%systemd_preun iscsi.service iscsid.service iscsid.socket iscsi-init.service

%postun
%systemd_postun_with_restart iscsi.service iscsid.service iscsid.socket iscsi-init.service

%post -n iscsiuio
%systemd_post iscsiuio.service iscsiuio.socket

%preun -n iscsiuio
%systemd_preun iscsiuio.service iscsiuio.socket

%postun -n iscsiuio
%systemd_postun_with_restart iscsiuio.service iscsiuio.socket

# TODO: fix tests.
%check

%files
%license COPYING
%doc README
%dir %{_sysconfdir}/iscsi
%{_sysconfdir}/iscsid.conf
%config(noreplace) %{_sysconfdir}/iscsi/iscsid.conf
%ghost %{_sysconfdir}/iscsi/initiatorname.iscsi
%dir %{_sharedstatedir}/iscsi
%dir %{_sharedstatedir}/iscsi/ifaces
%{_sharedstatedir}/iscsi/ifaces/iface.example
%{_unitdir}/iscsid.service
%{_unitdir}/iscsid.socket
%{_unitdir}/iscsi-init.service
%{_unitdir}/iscsi.service
%{_systemdgeneratordir}/ibft-rule-generator
%{_sbindir}/iscsid
%{_sbindir}/iscsiadm
%{_sbindir}/iscsi-iname
%{_sbindir}/iscsistart
%{_sbindir}/iscsi-gen-initiatorname
%{_sbindir}/iscsi_offload
%{_sbindir}/iscsi_discovery
%{_sbindir}/iscsi_fw_login
%{_mandir}/man8/iscsiadm.8*
%{_mandir}/man8/iscsid.8*
%{_mandir}/man8/iscsi-gen-initiatorname.8*
%{_mandir}/man8/iscsi-iname.8*
%{_mandir}/man8/iscsi_discovery.8*
%{_mandir}/man8/iscsi_fw_login.8*
%{_mandir}/man8/iscsistart.8*

%{_udevrulesdir}/50-iscsi-firmware-login.rules
%{_libdir}/libopeniscsiusr.so.*

%files -n iscsiuio
%{_sbindir}/iscsiuio
%{_sbindir}/brcm_iscsiuio
%{_mandir}/man8/iscsiuio.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/iscsiuio
%{_unitdir}/iscsiuio.service
%{_unitdir}/iscsiuio.socket

%files devel
%{_includedir}/libopeniscsiusr*.h
%{_mandir}/man3/*.3*
%{_libdir}/libopeniscsiusr.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
