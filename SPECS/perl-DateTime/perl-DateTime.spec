# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime
Version:        1.66
Release:        %autorelease
Summary:        Date and time object for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/dist/DateTime
#!RemoteAsset:  sha256:afabd686fb83d3ebf49ee453974f9122f3eec9b25ff8d2ddf4f12de92af1e5e2
Source0:        https://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(DateTime::Locale) >= 1.06
BuildRequires:  perl(DateTime::TimeZone) >= 2.44
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.26
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.50
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Specio::Subs)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel
BuildRequires:  perl(Clone)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Devel::StackTrace)

Requires:       perl(DateTime::Locale) >= 1.06
Requires:       perl(DateTime::TimeZone) >= 2.44
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(Params::ValidationCompiler) >= 0.26
Requires:       perl(Specio) >= 0.50

%description
DateTime is a class for the representation of date/time combinations, and
is part of the Perl DateTime project.

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS leaptab.txt perlcriticrc perltidyrc precious.toml README.md TODO

%changelog
%autochangelog
