# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mojo-DOM58
Version:        3.002
Release:        %autorelease
Summary:        Minimalistic HTML/XML DOM parser with CSS selectors
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Mojo-DOM58
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Exporter) >= 5.57

%description
Mojo::DOM58 is a minimalistic and relaxed pure-perl HTML/XML DOM parser
based on Mojo::DOM. It supports the HTML Living Standard and Extensible
Markup Language (XML) 1.0, and matching based on CSS3 selectors. It will
even try to interpret broken HTML and XML, so you should not use it for
validation.

%prep
%setup -q -n Mojo-DOM58-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md prereqs.yml README

%changelog
%autochangelog
