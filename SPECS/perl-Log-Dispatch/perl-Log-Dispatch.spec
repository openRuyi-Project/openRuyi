# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Log-Dispatch
Version:        2.71
Release:        %autorelease
Summary:        Dispatches messages to one or more outputs
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Log-Dispatch
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.32
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog) >= 0.28
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(Specio) >= 0.32
Requires:       perl(Sys::Syslog) >= 0.28

%description
This module manages a set of Log::Dispatch::* output objects that can be
logged to via a unified interface.

%prep
%setup -q -n Log-Dispatch-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md weaver.ini

%changelog
%autochangelog
