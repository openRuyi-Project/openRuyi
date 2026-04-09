# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Params-ValidationCompiler
Version:        0.31
Release:        %autorelease
Summary:        Build an optimized subroutine parameter validator once, use it forever
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Params-ValidationCompiler
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Params-ValidationCompiler-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor) >= 1.17
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.14
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(warnings)

Requires:       perl(Class::XSAccessor) >= 1.17
Requires:       perl(List::Util) >= 1.29
Requires:       perl(Sub::Util) >= 1.40

%description
This module creates a customized, highly efficient parameter checking
subroutine. It can handle named or positional parameters, and can return
the parameters as key/value pairs or a list of values.

%prep
%setup -q -n Params-ValidationCompiler-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md test-matrix.als

%changelog
%autochangelog
