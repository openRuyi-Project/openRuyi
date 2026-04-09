# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test2-Plugin-NoWarnings
Version:        0.10
Release:        %autorelease
Summary:        Fail if tests warn
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Test2-Plugin-NoWarnings
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test2) >= 1.302167
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Event)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(warnings)

Requires:       perl(Test2) >= 1.302167

%description
Loading this plugin causes your tests to fail if there any warnings while
they run. Each warning generates a new failing test and the warning content
is outputted via diag.

%prep
%setup -q -n Test2-Plugin-NoWarnings-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md

%changelog
%autochangelog
