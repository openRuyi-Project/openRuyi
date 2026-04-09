# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Class-Singleton
Version:        1.6
Release:        %autorelease
Summary:        Implementation of a "Singleton" class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Class-Singleton
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHAY/Class-Singleton-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This is the Class::Singleton module. A Singleton describes an object class
that can have only one instance in any system. An example of a Singleton
might be a print spooler or system registry. This module implements a
Singleton class from which other classes can be derived. By itself, the
Class::Singleton module does very little other than manage the
instantiation of a single object. In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

%prep
%setup -q -n Class-Singleton-%{version}

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
