# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-SomeUtils
Version:        0.59
Release:        %autorelease
Summary:        Provide the stuff missing in List::Util
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/List-SomeUtils
#!RemoteAsset:  sha256:fab30372e4c67bf5a46062da38d1d0c8756279feada866eb439fa29571a2dc7b
Source0:        https://www.cpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Implementation) >= 0.04
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(vars)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)

Requires:       perl(Module::Implementation) >= 0.04

%description
List::SomeUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md

%changelog
%autochangelog
