# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wpa_supplicant
Version:        2.11
Release:        %autorelease
Summary:        WPA/WPA2/IEEE 802.1X Supplicant
License:        BSD-3-Clause
URL:            http://w1.fi/wpa_supplicant/
VCS:            git:https://git.w1.fi/cgit/hostap/
#!RemoteAsset
Source0:        http://w1.fi/releases/wpa_supplicant-%{version}.tar.gz
Source1:        wpa_supplicant.conf
Source2:        wpa_supplicant.service
Source3:        wpa_supplicant.sysconfig
Source4:        wpa_supplicant.logrotate
BuildSystem:    autotools

BuildOption(build):  -C wpa_supplicant
BuildOption(build):  CXXFLAGS="${CXXFLAGS:-%optflags} -fPIE -DPIE"
BuildOption(build):  LDFLAGS="${LDFLAGS:-%optflags} -pie -Wl,-z,now"
BuildOption(install):  -C wpa_supplicant
BuildOption(install):  BINDIR=%{_sbindir}
BuildOption(install):  LIBDIR=%{_libdir}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  docbook-utils
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}

%description
wpa_supplicant is a WPA Supplicant for Linux, BSD and Windows with support
for WPA and WPA2 (IEEE 802.11i / RSN).

%conf
cp wpa_supplicant/defconfig wpa_supplicant/.config

%build -a
make -C wpa_supplicant eapol_test
make -C wpa_supplicant/doc/docbook man

%install -a
install -D -m 0600 %{SOURCE1} %{buildroot}%{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/wpa_supplicant.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/wpa_supplicant
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/wpa_supplicant

install -D -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf \
  %{buildroot}%{_datadir}/dbus-1/system.d/wpa_supplicant.conf
install -D -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service \
  %{buildroot}%{_datadir}/dbus-1/system-services/fi.w1.wpa_supplicant1.service

install -d %{buildroot}%{_mandir}/man{5,8}
install -m 0644 wpa_supplicant/doc/docbook/*.8 %{buildroot}%{_mandir}/man8
install -m 0644 wpa_supplicant/doc/docbook/*.5 %{buildroot}%{_mandir}/man5

%check
# No tests here.

%post
%systemd_post wpa_supplicant.service

%preun
%systemd_preun wpa_supplicant.service

%postun
%systemd_postun_with_restart wpa_supplicant.service

%files
%license COPYING
%doc README wpa_supplicant/ChangeLog wpa_supplicant/todo.txt wpa_supplicant/examples
%config(noreplace) %{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf
%config(noreplace) %{_sysconfdir}/sysconfig/wpa_supplicant
%config(noreplace) %{_sysconfdir}/logrotate.d/wpa_supplicant
%{_unitdir}/wpa_supplicant.service
%{_datadir}/dbus-1/system.d/wpa_supplicant.conf
%{_datadir}/dbus-1/system-services/fi.w1.wpa_supplicant1.service
%{_sbindir}/wpa_passphrase
%{_sbindir}/wpa_supplicant
%{_sbindir}/wpa_cli
%dir %{_sysconfdir}/wpa_supplicant
%{_mandir}/man8/wpa_supplicant.8*
%{_mandir}/man8/wpa_gui.8.gz
%{_mandir}/man8/wpa_priv.8*
%{_mandir}/man8/wpa_passphrase.8*
%{_mandir}/man8/wpa_cli.8*
%{_mandir}/man8/wpa_background.8*
%{_mandir}/man8/eapol_test.8*
%{_mandir}/man5/wpa_supplicant.conf.5*

%changelog
%autochangelog
