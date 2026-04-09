# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-PPI
Version:        1.283
Release:        %autorelease
Summary:        Parse, Analyze and Manipulate Perl (without perl)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/PPI
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MI/MITHALDU/PPI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5) >= 2.35
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.84
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(parent)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(strict)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::PP)

Requires:       perl(Clone) >= 0.30
Requires:       perl(Digest::MD5) >= 2.35
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Storable) >= 2.17
Requires:       perl(version) >= 0.77

%description
About this Document

%prep
%setup -q -n PPI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes dev_notes.txt README

%changelog
%autochangelog
