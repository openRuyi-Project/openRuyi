# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global openjadever 1.3.2
%global version_list "{3,4}.{0,1}-sgml 4.1.2-xml 4.{2,3,4,5}-{sgml,xml} 4.{2,3,4,5}-rng 4.{2,3,4,5}-xsd"
%global catalog_list "{3,4}.{0,1}-sgml 4.1.2-xml 4.{2,3,4,5}-{sgml,xml}"
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           docbook-dtds
Version:        1.0
Release:        %autorelease
Summary:        SGML and XML document type definitions for DocBook
License:        DocBook-DTD
URL:            https://www.oasis-open.org/docbook/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
#!RemoteAsset
Source1:        https://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
#!RemoteAsset
Source2:        https://www.oasis-open.org/docbook/sgml/4.0/docbk40.zip
#!RemoteAsset
Source3:        https://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
#!RemoteAsset
Source4:        https://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
#!RemoteAsset
Source5:        https://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
#!RemoteAsset
Source6:        https://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
#!RemoteAsset
Source7:        https://archive.docbook.org/sgml/4.3/docbook-4.3.zip
#!RemoteAsset
Source8:        https://archive.docbook.org/xml/4.3/docbook-xml-4.3.zip
#!RemoteAsset
Source9:        https://archive.docbook.org/sgml/4.4/docbook-4.4.zip
#!RemoteAsset
Source10:       https://archive.docbook.org/xml/4.4/docbook-xml-4.4.zip
#!RemoteAsset
Source11:       https://archive.docbook.org/sgml/4.5/docbook-4.5.zip
#!RemoteAsset
Source12:       https://archive.docbook.org/xml/4.5/docbook-xml-4.5.zip
#!RemoteAsset
Source13:       https://archive.docbook.org/rng/4.2/docbook-rng-4.2.zip
#!RemoteAsset
Source14:       https://archive.docbook.org/rng/4.3/docbook-rng-4.3.zip
#!RemoteAsset
Source15:       https://archive.docbook.org/rng/4.4/docbook-rng-4.4.zip
#!RemoteAsset
Source16:       https://archive.docbook.org/xsd/4.2/docbook-xsd-4.2.zip
#!RemoteAsset
Source17:       https://archive.docbook.org/xsd/4.3/docbook-xsd-4.3.zip
#!RemoteAsset
Source18:       https://archive.docbook.org/xsd/4.4/docbook-xsd-4.4.zip
# http://www.docbook.org/rng/4.5/ upstream archive unavailable
#!RemoteAsset
Source100:      https://archive.docbook.org/rng/4.5/calstblx.rnc
#!RemoteAsset
Source101:      https://archive.docbook.org/rng/4.5/calstblx.rng
#!RemoteAsset
Source102:      https://archive.docbook.org/rng/4.5/dbhierx.rnc
#!RemoteAsset
Source103:      https://archive.docbook.org/rng/4.5/dbhierx.rng
#!RemoteAsset
Source104:      https://archive.docbook.org/rng/4.5/dbnotnx.rnc
#!RemoteAsset
Source105:      https://archive.docbook.org/rng/4.5/dbnotnx.rng
#!RemoteAsset
Source106:      https://archive.docbook.org/rng/4.5/dbpoolx.rnc
#!RemoteAsset
Source107:      https://archive.docbook.org/rng/4.5/dbpoolx.rng
#!RemoteAsset
Source108:      https://archive.docbook.org/rng/4.5/docbook.rnc
#!RemoteAsset
Source109:      https://archive.docbook.org/rng/4.5/docbook.rng
#!RemoteAsset
Source110:      https://archive.docbook.org/rng/4.5/htmltblx.rnc
#!RemoteAsset
Source111:      https://archive.docbook.org/rng/4.5/htmltblx.rng
# http://www.docbook.org/xsd/4.5/ upstream archive unavailable
#!RemoteAsset
Source200:      https://archive.docbook.org/xsd/4.5/calstblx.xsd
#!RemoteAsset
Source201:      https://archive.docbook.org/xsd/4.5/dbhierx.xsd
#!RemoteAsset
Source202:      https://archive.docbook.org/xsd/4.5/dbnotnx.xsd
#!RemoteAsset
Source203:      https://archive.docbook.org/xsd/4.5/dbpoolx.xsd
#!RemoteAsset
Source204:      https://archive.docbook.org/xsd/4.5/docbook.xsd
#!RemoteAsset
Source205:      https://archive.docbook.org/xsd/4.5/htmltblx.xsd
#!RemoteAsset
Source206:      https://archive.docbook.org/xsd/4.5/xml.xsd
BuildArch:      noarch

BuildRequires:  unzip

Requires(post): %{_bindir}/xmlcatalog
Requires(postun): %{_bindir}/xmlcatalog
Requires(post): %{_bindir}/chmod
Requires(post): sed
Requires(postun): sed
Requires:       sgml-common
Requires:       xml-common

Provides:       docbook-dtd-xml = %{version}-%{release}
Provides:       docbook-dtd-sgml = %{version}-%{release}
Provides:       docbook-dtd30-sgml = %{version}-%{release}
Provides:       docbook-dtd31-sgml = %{version}-%{release}
Provides:       docbook-dtd40-sgml = %{version}-%{release}
Provides:       docbook-dtd41-sgml = %{version}-%{release}
Provides:       docbook-dtd412-xml = %{version}-%{release}
Provides:       docbook-dtd42-sgml = %{version}-%{release}
Provides:       docbook-dtd42-xml = %{version}-%{release}
Provides:       docbook-dtd43-sgml = %{version}-%{release}
Provides:       docbook-dtd43-xml = %{version}-%{release}
Provides:       docbook-dtd44-sgml = %{version}-%{release}
Provides:       docbook-dtd44-xml = %{version}-%{release}
Provides:       docbook-dtd45-sgml = %{version}-%{release}
Provides:       docbook-dtd45-xml = %{version}-%{release}

%patchlist
# Fix old catalog files
0001-docbook-dtd30-sgml-1.0.catalog.patch
0002-docbook-dtd31-sgml-1.0.catalog.patch
0003-docbook-dtd40-sgml-1.0.catalog.patch
0004-docbook-dtd41-sgml-1.0.catalog.patch
0005-docbook-dtd42-sgml-1.0.catalog.patch
# Fix euro sign in 4.2 dtds
0006-docbook-4.2-euro.patch
# Fix ISO entities in 4.3/4.4/4.5 SGML
0007-docbook-dtds-ents.patch
# Use system rewrite for web URL's in sgml catalogs to prevent reading from the network
0008-docbook-sgml-systemrewrite.patch
# Use XML at the end of public identificators of XML 4.1.2 ISO entities
0009-docbook-dtd412-entities.patch

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.

%prep
%setup -c -T
eval mkdir %{version_list}

unzip %{SOURCE0} -d 3.0-sgml
unzip %{SOURCE1} -d 3.1-sgml
unzip %{SOURCE2} -d 4.0-sgml
unzip %{SOURCE3} -d 4.1-sgml
unzip %{SOURCE4} -d 4.1.2-xml
unzip %{SOURCE5} -d 4.2-sgml
unzip %{SOURCE6} -d 4.2-xml
unzip %{SOURCE7} -d 4.3-sgml
unzip %{SOURCE8} -d 4.3-xml
unzip %{SOURCE9} -d 4.4-sgml
unzip %{SOURCE10} -d 4.4-xml
unzip %{SOURCE11} -d 4.5-sgml
unzip %{SOURCE12} -d 4.5-xml
unzip %{SOURCE13} -d 4.2-rng
unzip %{SOURCE14} -d 4.3-rng
unzip %{SOURCE15} -d 4.4-rng
unzip %{SOURCE16} -d 4.2-xsd
unzip %{SOURCE17} -d 4.3-xsd
unzip %{SOURCE18} -d 4.4-xsd
# No upstream archive for 4.5 rng, download individual files
cp %{SOURCE100} %{SOURCE101} %{SOURCE102} \
   %{SOURCE103} %{SOURCE104} %{SOURCE105} \
   %{SOURCE106} %{SOURCE107} %{SOURCE108} \
   %{SOURCE109} %{SOURCE110} %{SOURCE111} 4.5-rng/
# No upstream archive for 4.5 xsd, download individual files
cp %{SOURCE200} %{SOURCE201} %{SOURCE202} \
   %{SOURCE203} %{SOURCE204} %{SOURCE205} \
   %{SOURCE206} 4.5-xsd/

# Apply patches
%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0
%patch -P 3 -p0
%patch -P 4 -p0
%patch -P 5 -p0
%patch -P 6 -p0
%patch -P 7 -p0
%patch -P 8 -p0

# Increase NAMELEN
sed -e's,\(NAMELEN\s\+\)44\(\s\*\)\?,\1256,' -i.namelen */docbook.dcl

# Fix of \r\n issue from rpmlint
sed -i 's/\r//' */*.txt

if [ `id -u` -eq 0 ]; then
  %{_bindir}/chown -R root:root .
  %{_bindir}/chmod -R a+rX,g-w,o-w .
fi

%build
# Nothing to do

%install
# Creating a directory for SGML
eval mkdir -p %{buildroot}/etc/sgml

# Loop through sgml and xml formats
for fmt in sgml xml; do
  # Creating symbolic links for docbook catalog files
  ln -s $fmt-docbook-4.5.cat %{buildroot}/etc/sgml/$fmt-docbook.cat
done

# Loop through different versions of docbook
eval set %{version_list}
for dir in $@; do
  pushd $dir
  fmt=${dir#*-} ver=${dir%%-*} # Formatting and versioning

  # Directory paths for different formats
  case $fmt in
    sgml|xml)   DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-dtd-$ver ;;
    rng|xsd)    DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-$ver ;;
  esac

  # Installing files to the corresponding directories
  case $fmt in
    sgml)   mkdir -p $DESTDIR ; install *.dcl $DESTDIR ;;
    xml)    mkdir -p $DESTDIR/ent ; install ent/* $DESTDIR/ent ;;
    rng)    mkdir -p $DESTDIR ; install *.r* $DESTDIR ;;
    xsd)    mkdir -p $DESTDIR ; install *.xsd $DESTDIR;;
  esac
  popd
done

# Loop through different catalog versions
eval set %{catalog_list}
for dir in $@; do
  pushd $dir
  fmt=${dir#*-} ver=${dir%%-*} # Formatting and versioning
  DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-dtd-$ver

  # Installing dtd and mod files, along with the catalog file
  install *.dtd *.mod $DESTDIR
  install docbook.cat $DESTDIR/catalog
  popd

  # Creating ghost file for each format-version pair
  touch %{buildroot}/etc/sgml/$fmt-docbook-$ver.cat
done

# Workaround for missing support for --parents in rpm 4.11+
mkdir -p %{buildroot}%{_pkgdocdir}

# Copying text, ChangeLog, and README files to pkgdocdir with their parent directories
for i in */*.txt */ChangeLog */README; do
  cp -pr --parents $i %{buildroot}%{_pkgdocdir}
done

%post
catcmd='/usr/bin/xmlcatalog --noout'
xmlcatalog=%{_datadir}/sgml/docbook/xmlcatalog

# Clean up pre-docbook-dtds mess caused by broken trigger.
for v in 3.0 3.1 4.0 4.1 4.2 4.3 4.4 4.5
do
  if [ -f %{_sysconfdir}/sgml/sgml-docbook-$v.cat ]
  then
    $catcmd --sgml --del %{_sysconfdir}/sgml/sgml-docbook-$v.cat \
      %{_datadir}/sgml/openjade-%{openjadever}/catalog 2>/dev/null
  fi
done

# The STYLESHEETS/catalog command is for the case in which the style sheets
# were installed after another DTD but before this DTD
for STYLESHEETS in %{_datadir}/sgml/docbook/dsssl-stylesheets-*; do : ; done
case $STYLESHEETS in
  *-"*") STYLESHEETS= ;;
esac
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  sgmldir=%{_datadir}/sgml/docbook/$fmt-dtd-$ver
  # SGML catalog
  # Update the centralized catalog corresponding to this version of the DTD
  for cat_dir in %{_datadir}/sgml/sgml-iso-entities-8879.1986 $sgmldir $STYLESHEETS; do
    $catcmd --sgml --add %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat $cat_dir/catalog
  done
  # XML catalog
  if [ $fmt = xml -a -w $xmlcatalog ]; then
    while read f desc; do
      case $ver in 4.[45]) f=${f/-/} ;; esac
      $catcmd --add public "$desc" $sgmldir/$f $xmlcatalog
    done <<ENDENT
      ent/iso-pub.ent        ISO 8879:1986//ENTITIES Publishing//EN
      ent/iso-grk1.ent       ISO 8879:1986//ENTITIES Greek Letters//EN
      dbpoolx.mod    -//OASIS//ELEMENTS DocBook XML Information Pool V$ver//EN
      ent/iso-box.ent        ISO 8879:1986//ENTITIES Box and Line Drawing//EN
      docbookx.dtd   -//OASIS//DTD DocBook XML V$ver//EN
      ent/iso-grk3.ent       ISO 8879:1986//ENTITIES Greek Symbols//EN
      ent/iso-amsn.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN
      ent/iso-num.ent        ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN
      dbcentx.mod    -//OASIS//ENTITIES DocBook XML Character Entities V$ver//EN
      ent/iso-grk4.ent       ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN
      dbnotnx.mod    -//OASIS//ENTITIES DocBook XML Notations V$ver//EN
      ent/iso-dia.ent        ISO 8879:1986//ENTITIES Diacritical Marks//EN
      ent/iso-grk2.ent       ISO 8879:1986//ENTITIES Monotoniko Greek//EN
      dbgenent.mod   -//OASIS//ENTITIES DocBook XML Additional General Entities V$ver//EN
      dbhierx.mod    -//OASIS//ELEMENTS DocBook XML Document Hierarchy V$ver//EN
      ent/iso-amsa.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN
      ent/iso-amso.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN
      ent/iso-cyr1.ent       ISO 8879:1986//ENTITIES Russian Cyrillic//EN
      ent/iso-tech.ent       ISO 8879:1986//ENTITIES General Technical//EN
      ent/iso-amsc.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN
      soextblx.dtd   -//OASIS//DTD XML Exchange Table Model 19990315//EN
      calstblx.dtd   -//OASIS//DTD DocBook XML CALS Table Model V$ver//EN
      ent/iso-lat1.ent       ISO 8879:1986//ENTITIES Added Latin 1//EN
      ent/iso-amsb.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN
      ent/iso-lat2.ent       ISO 8879:1986//ENTITIES Added Latin 2//EN
      ent/iso-amsr.ent       ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN
      ent/iso-cyr2.ent       ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN
ENDENT
    for f in System URI; do
      $catcmd --add rewrite$f "http://www.oasis-open.org/docbook/xml/$ver" \
     $sgmldir $xmlcatalog
    done
  fi
done

# Historic versions of this scriptlet contained the following comment:
# <quote>
# Fix up SGML super catalog so that there isn't an XML DTD before an
# SGML one.  We need to do this (*sigh*) because xmlcatalog messes up
# the order of the lines, and SGML tools don't like to see XML things
# they aren't expecting.
# </quote>
# But the code that followed just found the first XML DTD and the first
# SGML DTD, swappinmg these two lines if the XML one preceded.
# But that only ensures that there is an SGML DTD before all XML ones.
# No one complained, so either this was enough, or the buggy SGML tools
# are long dead, or their users do not use bugzilla.
# Anyway, the following code, introduced in 1.0-46, does better: it ensures
# that all XML DTDs are after all SGML ones, by moving them to the end.
sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
  ' %{_sysconfdir}/sgml/catalog

# Finally, make sure everything in /etc/sgml is readable!
%{_bindir}/chmod a+r %{_sysconfdir}/sgml/*

%postun
# Remove entries only on removal of package
if [ "$1" = 0 ]; then
  catcmd='%{_bindir}/xmlcatalog --noout'
  xmlcatalog=%{_datadir}/sgml/docbook/xmlcatalog
  entities="
ent/iso-pub.ent
ent/iso-grk1.ent
dbpoolx.mod
ent/iso-box.ent
docbookx.dtd
ent/iso-grk3.ent
ent/iso-amsn.ent
ent/iso-num.ent
dbcentx.mod
ent/iso-grk4.ent
dbnotnx.mod
ent/iso-dia.ent
ent/iso-grk2.ent
dbgenent.mod
dbhierx.mod
ent/iso-amsa.ent
ent/iso-amso.ent
ent/iso-cyr1.ent
ent/iso-tech.ent
ent/iso-amsc.ent
soextblx.dtd
calstblx.dtd
ent/iso-lat1.ent
ent/iso-amsb.ent
ent/iso-lat2.ent
ent/iso-amsr.ent
ent/iso-cyr2.ent
  "
  eval set %{catalog_list}
  for dir
  do
    fmt=${dir#*-} ver=${dir%%-*}
    sgmldir=%{_datadir}/sgml/docbook/$fmt-dtd-$ver
    ## SGML catalog
    # Update the centralized catalog corresponding to this version of the DTD
    $catcmd --sgml --del %{_sysconfdir}/sgml/catalog %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat >/dev/null
    rm -f %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat
    ## XML catalog
    if [ $fmt = xml -a -w $xmlcatalog ]; then
      for f in $entities; do
        case $ver in 4.[45]) f=${f/-/} ;; esac
        $catcmd --del $sgmldir/$f $xmlcatalog >/dev/null
      done
      $catcmd --del $sgmldir $xmlcatalog >/dev/null
    fi
  done

  # See the comment attached to this command in the %%post scriptlet.
  sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
    ' %{_sysconfdir}/sgml/catalog
fi

%triggerin -- openjade >= %{openjadever}
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  %{_bindir}/xmlcatalog --sgml --noout --add %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat \
    %{_datadir}/sgml/openjade-%{openjadever}/catalog
done

%triggerun -- openjade >= %{openjadever}
[ $2 = 0 ] || exit 0
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  %{_bindir}/xmlcatalog --sgml --noout --del %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat \
    %{_datadir}/sgml/openjade-%{openjadever}/catalog
done

%files
%doc %{_pkgdocdir}
%{_datadir}/sgml/docbook/*ml-dtd-*
%{_datadir}/sgml/docbook/rng-*
%{_datadir}/sgml/docbook/xsd-*
%config(noreplace) %{_sysconfdir}/sgml/*ml-docbook.cat
%ghost %config(noreplace) %{_sysconfdir}/sgml/*ml-docbook-*.cat

%changelog
%autochangelog
