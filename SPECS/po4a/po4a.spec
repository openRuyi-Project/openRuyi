# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           po4a
Version:        0.74
Release:        %autorelease
Summary:        Tools for helping translation of documentation
License:        GPL-2.0-or-later
URL:            https://po4a.org/
VCS:            git:https://github.com/mquinson/po4a.git
#!RemoteAsset:  sha256:25fc323f2ba37bbd48c3af0ebf49952644b0e468261f98633e91219a838fe7c2
Source0:        https://github.com/mquinson/po4a/releases/download/v%{version}/po4a-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

# https://github.com/mquinson/po4a/issues/636
Patch0:         0001-Fix-msginit-compatibility-with-gettext-1.0.patch

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Locale::gettext) >= 1.01
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(SGMLS)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::WrapI18N)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::LineBreak)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  docbook-xsl
BuildRequires:  libxslt
# For tests
BuildRequires:  perl(Syntax::Keyword::Try)
BuildRequires:  opensp
BuildRequires:  docbook-dtds
# We need kpsewhich
BuildRequires:  texlive-latex

%description
po4a (PO for anything) eases the translation of documentation and other
textual content. It converts documentation to PO files for translation,
and then back to the original format from translated PO files.

%build -p
# Replace online docbook.xsl URL with local path for offline build
sed -i 's|http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl|file://%{_datadir}/sgml/docbook/xsl-stylesheets-1.79.2/manpages/docbook.xsl|' Po4aBuilder.pm

%files -f %{name}.files
%doc README* TODO changelog
%{_mandir}/*/man1/po4a*.1*
%{_mandir}/*/man1/msguntypot.1*
%{_mandir}/*/man3/Locale::Po4a::*.3*
%{_mandir}/*/man7/po4a.7*
%{_datadir}/locale/

%changelog
%autochangelog
