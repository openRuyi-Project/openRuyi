# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Util
Version:        1.09
Release:        %autorelease
Summary:        Module name tools and transformations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Util
#!RemoteAsset:  sha256:6cfbcb6a45064446ec8aa0ee1a7dddc420b54469303344187aef84d2c7f3e2c6
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralise some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.

%prep
%setup -q -n Module-Util-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README scripts
%license

%changelog
%autochangelog
