# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Tie-IxHash
Version:        1.23
Release:        %autorelease
Summary:        Ordered associative arrays for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Tie-IxHash
#!RemoteAsset:  sha256:fabb0b8c97e67c9b34b6cc18ed66f6c5e01c55b257dcf007555e0b027d4caf56
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Tie-IxHash-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)

%description
This Perl module implements Perl hashes that preserve the order in which
the hash elements were added. The order is not affected when values
corresponding to existing keys in the IxHash are changed. The elements can
also be set to any arbitrary supplied order. The familiar perl array
operations can also be performed on the IxHash.

%prep
%setup -q -n Tie-IxHash-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license

%changelog
%autochangelog
