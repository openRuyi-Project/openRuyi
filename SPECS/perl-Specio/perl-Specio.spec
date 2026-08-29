# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Specio
Version:        0.53
Release:        %autorelease
Summary:        Type constraints and coercions for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Specio
#!RemoteAsset:  sha256:0d0eecfb9e89bd0f5f710fac42e1200a882d513a862f98497eaef5927ac6c183
Source0:        https://www.cpan.org/authors/id/D/DR/DROLSKY/Specio-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(Ref::Util) >= 0.112
BuildRequires:  perl(Role::Tiny) >= 1.003003
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.83
BuildRequires:  perl(warnings)
BuildRequires:  perl(XString)

Requires:       perl(List::Util) >= 1.33
Requires:       perl(Ref::Util) >= 0.112
Requires:       perl(Role::Tiny) >= 1.003003
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Test::More) >= 0.96
Requires:       perl(version) >= 0.83

%description
The Specio distribution provides classes for representing type constraints
and coercion, along with syntax sugar for declaring them.

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md mise.toml perlcriticrc perltidyrc precious.toml README.md SECURITY.md SUPPORT.md TODO.md

%changelog
%autochangelog
