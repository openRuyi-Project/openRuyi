# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dropbear
Version:        2025.89
Release:        %autorelease
Summary:        A lightweight SSH server and client
License:        MIT
URL:            https://matt.ucc.asn.au/dropbear/dropbear.html
VCS:            git:https://github.com/mkj/dropbear
#!RemoteAsset
Source0:        https://matt.ucc.asn.au/dropbear/releases/dropbear-%{version}.tar.bz2
Source1:        dropbear.service
Source2:        dropbear-keygen.service
BuildSystem:    autotools

BuildOption(conf):  --enable-pam
BuildOption(conf):  --disable-bundled-libtom

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libtomcrypt)
BuildRequires:  pkgconfig(libtommath)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros
# for tests.
BuildRequires:  python3
%{?systemd_requires}

%description
Dropbear is a relatively small SSH server and client. It's particularly useful
for "embedded"-type Linux (or other Unix) systems, such as wireless routers.

%build -p
cat > localoptions.h <<EOT
#define SFTPSERVER_PATH "/usr/libexec/openssh/sftp-server"
EOT

%install -a
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_unitdir}
install -pm644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -pm644 %{SOURCE2} %{buildroot}%{_unitdir}/dropbear-keygen.service

# Tests require local network and the running user to be able to login,
# not feasible with mock restrictions
%check

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc CHANGES README.md
%license LICENSE
%dir %{_sysconfdir}/dropbear
%{_unitdir}/dropbear*
%{_bindir}/dropbearkey
%{_bindir}/dropbearconvert
%{_bindir}/dbclient
%{_sbindir}/dropbear
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
