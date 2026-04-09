# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           docbook-style-dsssl
Version:        1.79
Release:        %autorelease
Summary:        Norman Walsh's modular stylesheets for DocBook
License:        LicenseRef-DMIT
URL:            http://docbook.sourceforge.net/
#!RemoteAsset
Source0:        http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
Source1:        %{name}.Makefile
BuildArch:      noarch

# https://github.com/docbook/xslt10-stylesheets/issues/176
Patch0:         0001-docbook-style-xsl-non-recursive-string-subst.patch

BuildRequires:  perl
BuildRequires:  make

Requires:       docbook-dtds
Requires:       openjade
Requires:       sgml-common
Requires(post): sgml-common
Requires(preun): sgml-common

%description
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.

%prep
%setup -q -n docbook-dsssl-%{version}
cp %{SOURCE1} Makefile

%build

%install
DESTDIR=$RPM_BUILD_ROOT
make install BINDIR=$DESTDIR/usr/bin DESTDIR=$DESTDIR/usr/share/sgml/docbook/dsssl-stylesheets-%{version} MANDIR=$DESTDIR%{_mandir}
cd ..
ln -s dsssl-stylesheets-%{version} $DESTDIR/usr/share/sgml/docbook/dsssl-stylesheets

%post
for centralized in /etc/sgml/*-docbook-*.cat
do
  /usr/bin/install-catalog --add $centralized \
    /usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog \
    > /dev/null 2>/dev/null
done

%preun
if [ "$1" = "0" ]; then
  for centralized in /etc/sgml/*-docbook-*.cat
  do
    /usr/bin/install-catalog --remove $centralized /usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null 2>/dev/null
  done
fi
exit 0

%files
%doc BUGS README ChangeLog WhatsNew
%{_bindir}/collateindex.pl
%{_mandir}/man1/collateindex.pl.1*
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
%{_datadir}/sgml/docbook/dsssl-stylesheets

%changelog
%autochangelog
