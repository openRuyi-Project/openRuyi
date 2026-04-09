# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-TimeZone
Version:        2.65
Release:        %autorelease
Summary:        Time zone object base class and factory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DateTime-TimeZone
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Singleton) >= 1.03
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd) >= 3
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(parent)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)

Requires:       perl(Class::Singleton) >= 1.03
Requires:       perl(Cwd) >= 3
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::ValidationCompiler) >= 0.13

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which describes the
offset from GMT for a given time period.

%prep
%setup -q -n DateTime-TimeZone-%{version}

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
