# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# For the first time, we need to bootstrap this
# Change 0 to 1 after the first init build
%bcond bootstrap 1

Name:           perl-HTML-Tree
Version:        5.07
Release:        %autorelease
Summary:        Build and scan parse-trees of HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Tree
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/K/KE/KENTNL/HTML-Tree-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTML::Entities)
%if %{without bootstrap}
BuildRequires:  perl(HTML::FormatText)
%endif
BuildRequires:  perl(HTML::Parser) >= 3.46
BuildRequires:  perl(HTML::Tagset) >= 3.02
BuildRequires:  perl(integer)
BuildRequires:  perl(LWP::UserAgent) >= 5.815
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)

Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02
Requires:       perl(LWP::UserAgent) >= 5.815

%description
HTML-Tree is a suite of Perl modules for making parse trees out of HTML
source. It consists of mainly two modules, whose documentation you should
refer to: HTML::TreeBuilder and HTML::Element.

%prep
%setup -q -n HTML-Tree-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
