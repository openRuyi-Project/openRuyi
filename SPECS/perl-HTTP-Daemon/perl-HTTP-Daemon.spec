# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTTP-Daemon
Version:        6.17
Release:        %autorelease
Summary:        Simple http server class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Daemon
#!RemoteAsset:  sha256:16281580c40e23108d028434698b5d7d53637bf904c9df822481e253cbec920c
Source0:        https://www.cpan.org/authors/id/O/OA/OALDERS/HTTP-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::IP) >= 0.32
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Build::Tiny)

Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(LWP::MediaTypes) >= 6

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::IP, so you can perform socket operations directly on it too.

%files -f %{name}.files
%doc Changes CONTRIBUTING precious.toml README scripts

%changelog
%autochangelog
