# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond selinux 1
%bcond pam 1
%bcond audit 1

Name:           cronie
Version:        1.7.2
Release:        %autorelease
Summary:        Cron daemon for executing programs at set times
License:        GPL-2.0-or-later AND BSD-3-Clause AND BSD-2-Clause AND ISC AND LGPL-2.1-or-later
URL:            https://github.com/cronie-crond/cronie
#!RemoteAsset
Source:         %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/cronie-crond/cronie/issues/193
Patch0:         0001-make_error_func_prototype_complete.patch

BuildOption(conf):  --with-selinux=%{?with_selinux:yes}%{!?with_selinux:no}
BuildOption(conf):  --with-pam=%{?with_pam:yes}%{!?with_pam:no}
BuildOption(conf):  --with-audit=%{?with_audit:yes}%{!?with_audit:no}
BuildOption(conf):  --enable-anacron
BuildOption(conf):  --enable-pie

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  systemd
BuildRequires:  make
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif
%if %{with pam}
BuildRequires:  pkgconfig(pam)
%endif
%if %{with audit}
BuildRequires:  audit-devel
%endif

%if %{with selinux}
Requires:       libselinux
%endif
%if %{with pam}
Requires:       pam
%endif
%if %{with systemd}
%{?systemd_requires}
%endif
Requires(post): coreutils sed

%description
Cronie contains the standard UNIX daemon crond that runs specified programs at
scheduled times and related tools. It is a fork of the original vixie-cron and
has security and configuration enhancements like the ability to use pam and
SELinux.

%package        anacron
Summary:        Utility for running regular jobs
Requires(post): coreutils
Requires:       %{name} = %{version}-%{release}

%description    anacron
Anacron is part of cronie that is used for running jobs with regular
periodicity which do not have exact time of day of execution.

The default settings of anacron execute the daily, weekly, and monthly
jobs, but anacron allows setting arbitrary periodicity of jobs.

Using anacron allows running the periodic jobs even if the system is often
powered off and it also allows randomizing the time of the job execution
for better utilization of resources shared among multiple systems.

%install -a
mkdir -pm700 %{buildroot}%{_localstatedir}/spool/cron
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
mkdir -pm755 %{buildroot}%{_sysconfdir}/cron.d/
%if ! %{with pam}
   rm -f %{buildroot}%{_sysconfdir}/pam.d/crond
%endif
install -m 644 crond.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/crond
touch %{buildroot}%{_sysconfdir}/cron.deny
install -m 644 contrib/anacrontab %{buildroot}%{_sysconfdir}/anacrontab
install -c -m755 contrib/0hourly %{buildroot}%{_sysconfdir}/cron.d/0hourly
mkdir -pm 755 %{buildroot}%{_sysconfdir}/cron.hourly
install -c -m755 contrib/0anacron %{buildroot}%{_sysconfdir}/cron.hourly/0anacron
mkdir -p %{buildroot}/var/spool/anacron
touch %{buildroot}/var/spool/anacron/cron.daily
touch %{buildroot}/var/spool/anacron/cron.weekly
touch %{buildroot}/var/spool/anacron/cron.monthly
# install systemd initscript
install -m 644 -D contrib/cronie.systemd $RPM_BUILD_ROOT/usr/lib/systemd/system/crond.service

%post
%systemd_post crond.service

%post anacron
[ -e /var/spool/anacron/cron.daily ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.daily 2>/dev/null || :
[ -e /var/spool/anacron/cron.weekly ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.weekly 2>/dev/null || :
[ -e /var/spool/anacron/cron.monthly ] || install -m 0600 -D /dev/null /var/spool/anacron/cron.monthly 2>/dev/null || :

%preun
%systemd_preun crond.service

%postun
%systemd_postun_with_restart crond.service

%files
%doc AUTHORS README ChangeLog
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(755,root,root) %{_bindir}/crond
%attr(4755,root,root) %{_bindir}/crontab
%attr(755,root,root) %{_bindir}/cronnext
%{_mandir}/man8/crond.*
%{_mandir}/man8/cron.*
%{_mandir}/man5/crontab.*
%{_mandir}/man1/crontab.*
%{_mandir}/man1/cronnext.*
%dir %{_localstatedir}/spool/cron
%dir %{_sysconfdir}/cron.d
%if %{with pam}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/crond
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/crond
%config(noreplace,missingok) %{_sysconfdir}/cron.deny
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/0hourly
%attr(0644,root,root) /usr/lib/systemd/system/crond.service
%{_sbindir}/crond

%files anacron
%{_bindir}/anacron
%attr(0755,root,root) %{_sysconfdir}/cron.hourly/0anacron
%config(noreplace) %{_sysconfdir}/anacrontab
%dir /var/spool/anacron
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.daily
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.weekly
%ghost %attr(0600,root,root) %verify(not md5 size mtime) /var/spool/anacron/cron.monthly
%{_mandir}/man5/anacrontab.*
%{_mandir}/man8/anacron.*
%{_sbindir}/anacron

%changelog
%autochangelog
