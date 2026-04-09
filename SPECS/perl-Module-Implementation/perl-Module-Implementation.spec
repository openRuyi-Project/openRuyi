# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Implementation
Version:        0.09
Release:        %autorelease
Summary:        Loads one of several alternate underlying implementations for a module
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Module-Implementation
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Module-Implementation-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)

Requires:       perl(Module::Runtime) >= 0.012

%description
This module abstracts out the process of choosing one of several underlying
implementations for a module. This can be used to provide XS and pure Perl
implementations of a module, or it could be used to load an implementation
for a given OS or any other case of needing to provide multiple
implementations.

%prep
%setup -q -n Module-Implementation-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
