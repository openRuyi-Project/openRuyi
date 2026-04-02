# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           socat
Version:        1.8.1.1
Release:        %autorelease
Summary:        Bidirectional data relay between two data channels
License:        GPL-2.0-only
URL:            http://www.dest-unreach.org/socat/
VCS:            git:https://repo.or.cz/socat.git
#!RemoteAsset:  sha256:f68b602c80e94b4b7498d74ec408785536fe33534b39467977a82ab2f7f01ddb
Source:         http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-help
BuildOption(conf):  --enable-stdio
BuildOption(conf):  --enable-fdnum
BuildOption(conf):  --enable-file
BuildOption(conf):  --enable-creat
BuildOption(conf):  --enable-gopen
BuildOption(conf):  --enable-pipe
BuildOption(conf):  --enable-termios
BuildOption(conf):  --enable-unix
BuildOption(conf):  --enable-ip4
BuildOption(conf):  --enable-ip6
BuildOption(conf):  --enable-rawip
BuildOption(conf):  --enable-tcp
BuildOption(conf):  --enable-udp
BuildOption(conf):  --enable-listen
BuildOption(conf):  --enable-proxy
BuildOption(conf):  --enable-exec
BuildOption(conf):  --enable-system
BuildOption(conf):  --enable-pty
BuildOption(conf):  --enable-readline
BuildOption(conf):  --enable-openssl
BuildOption(conf):  --enable-sycls
BuildOption(conf):  --enable-filan
BuildOption(conf):  --enable-retry

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf

%description
Socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device, socket,
SSL socket, proxy CONNECT connection, file descriptor, line editor, or program.

%prep -a
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES

sed -i "s/FGREP=fgrep/FGREP='grep -F'/" configure
sed -i "s/fgrep/grep -F/" test.sh
sed -i "s/egrep/grep -E/" test.sh

%install -a

install -d %{buildroot}/%{_docdir}/socat
install -m 0644 *.sh %{buildroot}/%{_docdir}/socat/
echo ".so man1/socat.1" | gzip > %{buildroot}/%{_mandir}/man1/filan.1.gz
cp -a %{buildroot}/%{_mandir}/man1/filan.1.gz %{buildroot}/%{_mandir}/man1/procan.1.gz

# No test suite.
%check

%files
%license COPYING*
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ PORTING README SECURITY
%{_bindir}/socat*
%{_bindir}/filan
%{_bindir}/procan
%{_mandir}/man1/*
%{_docdir}/socat/*.sh

%changelog
%{?autochangelog}
