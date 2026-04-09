# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DynaLoader-Functions
Version:        0.004
Release:        %autorelease
Summary:        Deconstructed dynamic C library loading
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DynaLoader-Functions
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-%{version}.tar.gz

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module provides a function-based interface to dynamic loading as used
by Perl. Some details of dynamic loading are very platform-dependent, so
correct use of these functions requires the programmer to be mindful of the
space of platform variations.

%prep
%setup -q -n DynaLoader-Functions-%{version}

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
