# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mock-Config
Version:        0.05
Release:        %autorelease
Summary:        Mock::Config Perl module
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Mock-Config
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RU/RURBAN/Mock-Config-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
use Mock::Config; Mock::Config->import(startperl => ''); print
$Config{startperl}, ' mocked to empty'; Mock::Config->unimport;

%prep
%setup -q -n Mock-Config-%{version}

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
