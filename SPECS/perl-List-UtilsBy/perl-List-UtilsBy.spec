# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-List-UtilsBy
Version:        0.12
Release:        %autorelease
Summary:        Higher-order list utility functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/List-UtilsBy
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/List-UtilsBy-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Exporter) >= 5.57

%description
This module provides a number of list utility functions, all of which take
an initial code block to control their behaviour. They are variations on
similar core perl or List::Util functions of similar names, but which use
the block to control their behaviour. For example, the core Perl function
sort takes a list of values and returns them, sorted into order by their
string value. The "sort_by" function sorts them according to the string
value returned by the extra function, when given each value.

%prep
%setup -q -n List-UtilsBy-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
