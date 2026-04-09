# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sysstat
Version:        12.7.8
Release:        %autorelease
Summary:        Performance monitoring tools for Linux
License:        GPL-2.0-or-later
URL:            https://sysstat.github.io/
VCS:            git:https://github.com/sysstat/sysstat.git
#!RemoteAsset
Source0:        https://github.com/sysstat/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-install-cron
BuildOption(conf):  --enable-copy-only
BuildOption(conf):  --disable-file-attr
BuildOption(conf):  --disable-stripping
BuildOption(conf):  --with-systemdsystemunitdir='%{_unitdir}'
BuildOption(conf):  --with-systemdsleepdir='%{_unitdir}-sleep'
BuildOption(conf):  sadc_options="-S DISK"
BuildOption(conf):  history="28"
BuildOption(conf):  compressafter="31"

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  lm_sensors-devel
BuildRequires:  systemd
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       findutils
Requires:       xz
%{?systemd_requires}

%description
The sysstat package contains various utilities, common to many commercial
Unixes, to monitor system performance and usage activity:
  - iostat reports CPU statistics and input/output statistics for block
    devices and partitions.
  - mpstat reports individual or combined processor related statistics.
  - pidstat reports statistics for Linux tasks (processes) : I/O, CPU,
    memory, etc.
  - tapestat reports statistics for tape drives connected to the system.
  - cifsiostat reports CIFS statistics.
Sysstat also contains tools you can schedule via cron or systemd to collect
and historize performance and activity data:
  - sar collects, reports and saves system activity information (see below
    a list of metrics collected by sar).
  - sadc is the system activity data collector, used as a backend for sar.
  - sa1 collects and stores binary data in the system activity daily data
    file. It is a front end to sadc designed to be run from cron or systemd.
  - sa2 writes a summarized daily activity report. It is a front end to sar
    designed to be run from cron or systemd.
  - sadf displays data collected by sar in multiple formats (CSV, XML, JSON,
    etc.) and can be used for data exchange with other programs. This command
    can also be used to draw graphs for the various activities collected by
    sar using SVG (Scalable Vector Graphics) format.

%install -a
# Do not install the license as documentation
rm %{buildroot}%{_docdir}/%{name}/COPYING

%find_lang %{name} --generate-subpackages

%check
./do_test

%post
%systemd_post sysstat.service sysstat-collect.timer sysstat-summary.timer

%preun
%systemd_preun sysstat.service sysstat-collect.timer sysstat-summary.timer
if [[ $1 -eq 0 ]]; then
    # Remove sa logs if removing sysstat completely
    rm -rf %{_localstatedir}/log/sa/*
fi

%postun
%systemd_postun sysstat.service sysstat-collect.timer sysstat-summary.timer

%files
%license COPYING
%doc CHANGES CREDITS FAQ.md README.md
%config(noreplace) %{_sysconfdir}/sysconfig/sysstat
%config(noreplace) %{_sysconfdir}/sysconfig/sysstat.ioconf
%{_bindir}/*
%{_libdir}/sa
%{_unitdir}/../*
%{_systemd_util_dir}/system-sleep/sysstat*
%{_localstatedir}/log/sa
%{_mandir}/man*/*

%changelog
%autochangelog
