# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTTP-Tiny
Version:        0.090
Release:        %autorelease
Summary:        Small, simple, correct HTTP/1.1 client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Tiny
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/H/HA/HAARG/HTTP-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::CookieJar) >= 0.001
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP) >= 0.32
BuildRequires:  perl(IO::Socket::SSL) >= 1.968
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::SSLeay) >= 1.49
BuildRequires:  perl(open)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)

Requires:       perl(HTTP::CookieJar) >= 0.001
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(IO::Socket::SSL) >= 1.968
Requires:       perl(Net::SSLeay) >= 1.49

%description
This is a very simple HTTP/1.1 client, designed for doing simple requests
without the overhead of a large framework like LWP::UserAgent.

%prep
%setup -q -n HTTP-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README

%changelog
%autochangelog
