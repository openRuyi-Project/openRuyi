# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTTP-CookieJar
Version:        0.014
Release:        %autorelease
Summary:        Minimalist HTTP user agent cookie jar
License:        Apache-2.0
URL:            https://metacpan.org/dist/HTTP-CookieJar
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mozilla::PublicSuffix)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)

Requires:       perl(Time::Local)

%description
This module implements a minimalist HTTP user agent cookie jar in
conformance with RFC 6265.

%prep
%setup -q -n HTTP-CookieJar-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README tidyall.ini

%changelog
%autochangelog
