# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global snap_release 20190603

Name:           crontabs
Version:        1.11
Release:        %autorelease
Summary:        Root crontab files used to schedule the execution of programs
License:        LicenseRef-openRuyi-Public-Domain and GPL-2.0-or-later
URL:            https://github.com/cronie-crond/crontabs
#!RemoteAsset
Source0:        https://github.com/cronie-crond/crontabs/releases/download/%{name}-%{snap_release}/%{name}-%{version}-%{snap_release}git.tar.gz
BuildArch:      noarch

Requires:       sed

Recommends:     cronie

%description
A crontab file contains instructions to the cron daemon
of the general form: 'run this command at  this  time  on
this  date'.   Each  user has their own crontab, and com-
mands in any given crontab will be executed  as  the  user
who  owns  the  crontab.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/cron.{hourly,daily,weekly,monthly}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man4/

install -m 644 ./crontab %{buildroot}%{_sysconfdir}/crontab
install -m 755 ./run-parts %{buildroot}%{_bindir}/run-parts
install -m 644 ./*.4 %{buildroot}%{_mandir}/man4/

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
touch %{buildroot}%{_sysconfdir}/sysconfig/run-parts

%files
%license COPYING
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/{crontab,sysconfig/run-parts}
%dir %{_sysconfdir}/cron.{hourly,daily,weekly,monthly}
%{_bindir}/run-parts
%{_mandir}/man4/*

%changelog
%autochangelog
