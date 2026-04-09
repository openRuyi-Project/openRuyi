# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Diff
Version:        1.45
Release:        %autorelease
Summary:        Perform diffs on files and record sets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Diff
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/Text-Diff-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Algorithm::Diff) >= 1.19

%description
diff() provides a basic set of services akin to the GNU diff utility. It is
not anywhere near as feature complete as GNU diff, but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's diff executable for small files, and
generally slower on larger files.

%prep
%setup -q -n Text-Diff-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
