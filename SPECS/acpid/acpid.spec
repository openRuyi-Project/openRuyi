# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           acpid
Version:        2.0.34
Release:        %autorelease
Summary:        Daemon for Advanced Configuration and Power Interface
License:        GPL-2.0-only
URL:            https://sourceforge.net/projects/acpid2/
#!RemoteAsset:  sha256:2d095c8cfcbc847caec746d62cdc8d0bff1ec1bc72ef7c674c721e04da6ab333
Source0:        https://downloads.sourceforge.net/project/acpid2/acpid-%{version}.tar.xz
Source1:        acpid.path
Source2:        acpid.service
Source3:        acpid.socket
Source4:        acpid.default
BuildSystem:    autotools

BuildOption(build):  LD=ld.bfd

BuildRequires:  make

%description
Advanced Configuration and Power Interface event daemon Modern computers
support the Advanced Configuration and Power Interface (ACPI) to allow
intelligent power management on your system and to query battery and
configuration status.

ACPID is a completely flexible, totally extensible daemon for delivering
ACPI events. It listens on netlink interface (or on the deprecated file
/proc/acpi/event), and when an event occurs, executes programs to handle
the event. The programs it executes are configured through a set of
configuration files, which can be dropped into place by packages or by the
admin.

%install -a
install -D -m 644 samples/power %{buildroot}/etc/acpi/events/power
install -D -m 755 samples/power.sh %{buildroot}/etc/acpi/power.sh
install -D -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/acpid.path
install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/acpid.service
install -D -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/acpid.socket
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/default/acpid

%check
# No tests

%post
%systemd_post acpid.path acpid.socket

%preun
%systemd_preun acpid.path acpid.socket

%postun
%systemd_postun acpid.path acpid.socket

%files
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/TESTPLAN
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/Changelog
%license %{_docdir}/%{name}/COPYING
%{_bindir}/acpi_listen
%config(noreplace) %{_sysconfdir}/acpi/events/power
%config(noreplace) %{_sysconfdir}/acpi/power.sh
%config(noreplace) %{_sysconfdir}/default/acpid
%{_datadir}/man/man8/acpi_listen.8.gz
%{_datadir}/man/man8/acpid.8.gz
%{_datadir}/man/man8/kacpimon.8.gz
%{_sbindir}/acpid
%{_sbindir}/kacpimon
%{_unitdir}/acpid.path
%{_unitdir}/acpid.service
%{_unitdir}/acpid.socket

%changelog
%autochangelog
