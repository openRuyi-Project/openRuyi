# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Params-Validate
Version:        1.31
Release:        %autorelease
Summary:        Validate method/function parameters
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Params-Validate
#!RemoteAsset:  sha256:1bf2518ef2c4869f91590e219f545c8ef12ed53cf313e0eb5704adf7f1b2961e
Source0:        https://www.cpan.org/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor optimize="%{optflags}"
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.10
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

Requires:       perl(Scalar::Util) >= 1.10

%description
I would recommend you consider using Params::ValidationCompiler instead.
That module, despite being pure Perl, is significantly faster than this
one, at the cost of having to adopt a type system such as Specio,
Type::Tiny, or the one shipped with Moose.

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc README.md tidyall.ini TODO weaver.ini

%changelog
%autochangelog
