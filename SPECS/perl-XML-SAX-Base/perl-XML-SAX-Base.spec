# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-SAX-Base
Version:        1.09
Release:        %autorelease
Summary:        Base class SAX Drivers and Filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-SAX-Base
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/G/GR/GRANTM/XML-SAX-Base-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88

%description
This module has a very simple task - to be a base class for PerlSAX drivers
and filters. It's default behaviour is to pass the input directly to the
output unchanged. It can be useful to use this module as a base class so
you don't have to, for example, implement the characters() callback.

%prep
%setup -q -n XML-SAX-Base-%{version}

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
