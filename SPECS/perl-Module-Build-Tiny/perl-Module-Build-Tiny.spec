# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Build-Tiny
Version:        0.052
Release:        %autorelease
Summary:        Tiny replacement for Module::Build
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Build-Tiny
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Requirements::Dynamic)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Config) >= 0.003
BuildRequires:  perl(ExtUtils::Helpers) >= 0.020
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(strict)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

Requires:       perl(Exporter) >= 5.57
Requires:       perl(ExtUtils::Config) >= 0.003
Requires:       perl(ExtUtils::Helpers) >= 0.020
Requires:       perl(ExtUtils::InstallPaths) >= 0.002
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(JSON::PP) >= 2

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file
to drive distribution configuration, build, test and installation.
Traditionally, Build.PL uses Module::Build as the underlying build system.
This module provides a simple, lightweight, drop-in replacement.

%prep
%setup -q -n Module-Build-Tiny-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README Todo

%changelog
%autochangelog
