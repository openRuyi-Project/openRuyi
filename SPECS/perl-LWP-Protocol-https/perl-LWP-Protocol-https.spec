# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-LWP-Protocol-https
Version:        6.15
Release:        %autorelease
Summary:        Provide https support for LWP::UserAgent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/LWP-Protocol-https
#!RemoteAsset:  sha256:44eec2da147ba0511090871b0ca82f69794376bc31e8c76d1040961ba57f59b8
Source0:        https://www.cpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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
BuildRequires:  perl(Try::Tiny)

Requires:       perl(IO::Socket::SSL) >= 1.970
Requires:       perl(LWP::UserAgent) >= 6.06
Requires:       perl(Net::HTTPS) >= 6

%description
The LWP::Protocol::https module provides support for using https schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%files -f %{name}.files
%doc Changes CONTRIBUTING.md Install perlcriticrc perltidyrc tidyall.ini

%changelog
%autochangelog
