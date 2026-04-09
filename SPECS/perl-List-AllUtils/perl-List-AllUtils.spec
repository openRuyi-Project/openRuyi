# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-AllUtils
Version:        0.19
Release:        %autorelease
Summary:        Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package
License:        Artistic-2.0
URL:            https://metacpan.org/dist/List-AllUtils
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::SomeUtils) >= 0.58
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(List::UtilsBy) >= 0.11
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(List::SomeUtils) >= 0.58
Requires:       perl(List::Util) >= 1.56
Requires:       perl(List::UtilsBy) >= 0.11

%description
Are you sick of trying to remember whether a particular helper is defined
in List::Util, List::SomeUtils or List::UtilsBy? I sure am. Now you don't
have to remember. This module will export all of the functions that either
of those three modules defines.

%prep
%setup -q -n List-AllUtils-%{version}

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
