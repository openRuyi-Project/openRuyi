# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-LWP-Protocol-https
Version:        6.14
Release:        %autorelease
Summary:        Provide https support for LWP::UserAgent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/LWP-Protocol-https
#!RemoteAsset
Source0:        https://www.cpan.org/modules/by-module/LWP/LWP-Protocol-https-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL) >= 1.970
BuildRequires:  perl(IO::Socket::SSL::Utils)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::UserAgent) >= 6.06
BuildRequires:  perl(Net::HTTPS) >= 6
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(warnings)

Requires:       perl(IO::Socket::SSL) >= 1.970
Requires:       perl(LWP::UserAgent) >= 6.06
Requires:       perl(Net::HTTPS) >= 6

%description
The LWP::Protocol::https module provides support for using https schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%prep
%setup -q -n LWP-Protocol-https-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md Install perlcriticrc perltidyrc tidyall.ini

%changelog
%autochangelog
