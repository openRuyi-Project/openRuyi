# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Path-Tiny
Version:        0.150
Release:        %autorelease
Summary:        File path utility
License:        Apache-2.0
URL:            https://metacpan.org/dist/Path-Tiny
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Path-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest) >= 1.03
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA) >= 5.45
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec) >= 0.86
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Unicode::UTF8) >= 0.58
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)

Requires:       perl(Digest) >= 1.03
Requires:       perl(Digest::SHA) >= 5.45
Requires:       perl(Exporter) >= 5.57
Requires:       perl(File::Path) >= 2.07
Requires:       perl(File::Spec) >= 0.86
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(Unicode::UTF8) >= 0.58

%description
This module provides a small, fast utility for working with file paths. It
is friendlier to use than File::Spec and provides easy access to functions
from several other core file handling modules. It aims to be smaller and
faster than many alternatives on CPAN, while helping people do many common
things in consistent and less error-prone ways.

%prep
%setup -q -n Path-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.mkdn perlcritic.rc README tidyall.ini

%changelog
%autochangelog
