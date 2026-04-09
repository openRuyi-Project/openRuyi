# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Which
Version:        1.27
Release:        %autorelease
Summary:        Perl implementation of the which utility as an API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Which
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/File-Which-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.47

%description
File::Which finds the full or relative paths to executable programs on the
system. This is normally the function of which utility. which is typically
implemented as either a program or a built in shell command. On some
platforms, such as Microsoft Windows it is not provided as part of the core
operating system. This module provides a consistent API to this
functionality regardless of the underlying platform.

%prep
%setup -q -n File-Which-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc author.yml Changes perlcriticrc README

%changelog
%autochangelog
