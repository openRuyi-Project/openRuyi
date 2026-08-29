# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Socket-IP
Version:        0.44
Release:        %autorelease
Summary:        Family-neutral IP socket supporting both IPv4 and IPv6
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Socket-IP
#!RemoteAsset:  sha256:dc39242154baf276a9b4802a2a56b9e769a8ec67b4c2fb7e089b68e3666cf289
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Socket) >= 1.97
BuildRequires:  perl(Test2::V0)

Requires:       perl(Socket) >= 1.97

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, intended as a replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way. For a
list of known differences, see the IO::Socket::INET INCOMPATIBILITIES
section below.

%files -f %{name}.files
%doc Changes examples README

%changelog
%autochangelog
