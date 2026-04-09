# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-FFI-CheckLib
Version:        0.31
Release:        %autorelease
Summary:        Check that a library is available for FFI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/FFI-CheckLib
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/FFI-CheckLib-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require::EnvVar) >= 0.000121
BuildRequires:  perl(Test2::Require::Module) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121

Requires:       perl(List::Util) >= 1.33

%description
This module checks whether a particular dynamic library is available for
FFI to use. It is modeled heavily on Devel::CheckLib, but will find dynamic
libraries even when development packages are not installed. It also
provides a find_lib function that will return the full path to the found
dynamic library, which can be feed directly into FFI::Platypus or another
FFI system.

%prep
%setup -q -n FFI-CheckLib-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc author.yml Changes perlcriticrc README

%changelog
%autochangelog
