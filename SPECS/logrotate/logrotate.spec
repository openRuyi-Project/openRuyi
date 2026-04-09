# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           logrotate
Version:        3.22.0
Release:        %autorelease
Summary:        Rotates, compresses, removes and mails system log files
License:        GPL-2.0-or-later
URL:            https://github.com/logrotate/logrotate
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/logrotate-%{version}.tar.xz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/logrotate-%{version}.tar.xz.asc
BuildSystem:    autotools

BuildOption(conf):  --with-state-file-path=%{_localstatedir}/lib/logrotate/logrotate.status

BuildRequires:  acl
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(popt)
BuildRequires:  systemd-rpm-macros

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.

Install the logrotate package if you need a utility to deal with the
log files on your system.

%conf -p
autoreconf -fiv

%install -a
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/logrotate

install -p -m 644 examples/logrotate.conf $RPM_BUILD_ROOT%{_sysconfdir}/
install -p -m 644 examples/{b,w}tmp $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/
install -p -m 644 examples/logrotate.{service,timer} $RPM_BUILD_ROOT%{_unitdir}/

%pre
# If /var/lib/logrotate/logrotate.status does not exist, create it and copy
# the /var/lib/logrotate.status in it (if it exists). We have to do that in pre
# script, otherwise the /var/lib/logrotate/logrotate.status would not be there,
# because during the update, it is removed/renamed.
if [ ! -d %{_localstatedir}/lib/logrotate/ -a -f %{_localstatedir}/lib/logrotate.status ]; then
 mkdir -p %{_localstatedir}/lib/logrotate
 cp -a %{_localstatedir}/lib/logrotate.status %{_localstatedir}/lib/logrotate
fi

%post
%systemd_post logrotate.{service,timer}

%preun
%systemd_preun logrotate.{service,timer}

%files
%license COPYING
%doc ChangeLog.md
%{_sbindir}/logrotate
%{_unitdir}/logrotate.{service,timer}
%{_mandir}/man8/logrotate.8*
%{_mandir}/man5/logrotate.conf.5*
%config(noreplace) %{_sysconfdir}/logrotate.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/{b,w}tmp
%dir %{_localstatedir}/lib/logrotate
%ghost %verify(not size md5 mtime) %attr(0640, root, root) %{_localstatedir}/lib/logrotate/logrotate.status

%changelog
%autochangelog
