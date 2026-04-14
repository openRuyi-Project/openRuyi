# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Hash-MoreUtils
Version:        0.06
Release:        %autorelease
Summary:        Provide the stuff missing in Hash::Util
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-MoreUtils
#!RemoteAsset:  sha256:db9a8fb867d50753c380889a5e54075651b5e08c9b3b721cb7220c0883547de8
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.90

%description
Similar to List::MoreUtils, Hash::MoreUtils contains trivial but commonly-
used functionality for hashes.

%prep
%setup -q -n Hash-MoreUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
