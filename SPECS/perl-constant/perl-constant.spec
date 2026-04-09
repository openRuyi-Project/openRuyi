# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-constant
Version:        1.33
Release:        %autorelease
Summary:        Perl pragma to declare constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/constant
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/constant-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
This pragma allows you to declare constants at compile-time.

%prep
%setup -q -n constant-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
