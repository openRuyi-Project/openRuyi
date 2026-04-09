# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tftp
Version:        5.3
Release:        %autorelease
Summary:        The client for the Trivial File Transfer Protocol (TFTP)
License:        BSD-4-Clause-UC
URL:            http://www.kernel.org/pub/software/network/tftp/
VCS:            git:https://kernel.googlesource.com/pub/scm/network/tftp/tftp-hpa
#!RemoteAsset
Source0:        https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git/snapshot/tftp-hpa-%{version}.tar.gz
Source1:        tftp.socket
Source2:        tftp.service
BuildSystem:    autotools

BuildOption(install):  INSTALLROOT=%{buildroot}
BuildOption(install):  SBINDIR=%{_sbindir}
BuildOption(install):  MANDIR=%{_mandir}

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(readline)

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations. The tftp package provides the user
interface for TFTP, which allows users to transfer files to and from a
remote machine.

%package        server
Summary:        The server for the Trivial File Transfer Protocol (TFTP)
%{?systemd_requires}

%description    server
The Trivial File Transfer Protocol (TFTP) server is normally used only for
booting diskless workstations.

%conf -p
autoreconf -fiv

%install -a
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/tftp.socket
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/tftp.service

install -d -m 0755 %{buildroot}%{_localstatedir}/lib/tftpboot

# No tests.
%check

%post server
%systemd_post tftp.socket

%preun server
%systemd_preun tftp.socket

%postun server
%systemd_postun_with_restart tftp.socket

%files
%doc README README.security CHANGES
%{_bindir}/tftp
%{_mandir}/man1/*

%files server
%doc README README.security CHANGES
%dir %{_localstatedir}/lib/tftpboot
%{_sbindir}/in.tftpd
%{_mandir}/man8/*
%{_unitdir}/*

%changelog
%autochangelog
