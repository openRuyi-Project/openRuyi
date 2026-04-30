# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Mask
Version:        0.06
Release:        %autorelease
Summary:        Pretend certain modules are not installed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Mask
#!RemoteAsset:  sha256:2d73f81ff21c9fa28102791e546ff257164b3025f7832544c8223fb87c1e7e77
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Mask-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Module::Util) >= 1.00
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(Test::Pod) >= 1.14
Requires:       perl(Test::Pod::Coverage) >= 1.04

%description
Sometimes you need to test what happens when a given module is not
installed. This module provides a way of temporarily hiding installed
modules from perl's require mechanism. The Module::Mask object adds itself
to @INC and blocks require calls to restricted modules.

%prep
%setup -q -n Module-Mask-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license

%changelog
%autochangelog
