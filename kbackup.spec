#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kbackup
Version  : 21.04.2
Release  : 31
URL      : https://download.kde.org/stable/release-service/21.04.2/src/kbackup-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/kbackup-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/kbackup-21.04.2.tar.xz.sig
Summary  : kbackup is an application which lets you back up your data in a simple, user friendly way.
Group    : Development/Tools
License  : GPL-2.0
Requires: kbackup-bin = %{version}-%{release}
Requires: kbackup-data = %{version}-%{release}
Requires: kbackup-license = %{version}-%{release}
Requires: kbackup-locales = %{version}-%{release}
Requires: kbackup-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data

%description
KBackup is a program that lets you back up any directories or files,
whereby it uses an easy to use directory tree to select the things to back up.
 
The program was designed to be very simple in its use
so that it can be used by non-computer experts.

It can do full- and incremental backups.
 
The storage format is the well known TAR format, whereby the data
is still stored in compressed format (bzip2 or gzip).

Included Languages:
- User interface:
  English, German, French, Italian, Russian, Slovak, Portuguese, Spanish, Swedish
- Handbook:
  English, German, French

%package bin
Summary: bin components for the kbackup package.
Group: Binaries
Requires: kbackup-data = %{version}-%{release}
Requires: kbackup-license = %{version}-%{release}

%description bin
bin components for the kbackup package.


%package data
Summary: data components for the kbackup package.
Group: Data

%description data
data components for the kbackup package.


%package doc
Summary: doc components for the kbackup package.
Group: Documentation
Requires: kbackup-man = %{version}-%{release}

%description doc
doc components for the kbackup package.


%package license
Summary: license components for the kbackup package.
Group: Default

%description license
license components for the kbackup package.


%package locales
Summary: locales components for the kbackup package.
Group: Default

%description locales
locales components for the kbackup package.


%package man
Summary: man components for the kbackup package.
Group: Default

%description man
man components for the kbackup package.


%prep
%setup -q -n kbackup-21.04.2
cd %{_builddir}/kbackup-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623366831
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623366831
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbackup
cp %{_builddir}/kbackup-21.04.2/COPYING %{buildroot}/usr/share/package-licenses/kbackup/4778e718b2212917a612ca048ce876fb95dfa04e
pushd clr-build
%make_install
popd
%find_lang kbackup

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kbackup

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kbackup.desktop
/usr/share/icons/hicolor/16x16/apps/kbackup.png
/usr/share/icons/hicolor/16x16/mimetypes/text-x-kbp.png
/usr/share/icons/hicolor/22x22/actions/kbackup_cancel.png
/usr/share/icons/hicolor/22x22/actions/kbackup_runs.png
/usr/share/icons/hicolor/22x22/actions/kbackup_start.png
/usr/share/icons/hicolor/32x32/apps/kbackup.png
/usr/share/icons/hicolor/32x32/mimetypes/text-x-kbp.png
/usr/share/kxmlgui5/kbackup/kbackupui.rc
/usr/share/metainfo/org.kde.kbackup.appdata.xml
/usr/share/mime-packages/kbackup.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kbackup/index.cache.bz2
/usr/share/doc/HTML/ca/kbackup/index.docbook
/usr/share/doc/HTML/ca/kbackup/mainwindow.png
/usr/share/doc/HTML/de/kbackup/index.cache.bz2
/usr/share/doc/HTML/de/kbackup/index.docbook
/usr/share/doc/HTML/en/kbackup/index.cache.bz2
/usr/share/doc/HTML/en/kbackup/index.docbook
/usr/share/doc/HTML/en/kbackup/mainwindow.png
/usr/share/doc/HTML/it/kbackup/index.cache.bz2
/usr/share/doc/HTML/it/kbackup/index.docbook
/usr/share/doc/HTML/nl/kbackup/index.cache.bz2
/usr/share/doc/HTML/nl/kbackup/index.docbook
/usr/share/doc/HTML/sv/kbackup/index.cache.bz2
/usr/share/doc/HTML/sv/kbackup/index.docbook
/usr/share/doc/HTML/uk/kbackup/index.cache.bz2
/usr/share/doc/HTML/uk/kbackup/index.docbook
/usr/share/doc/HTML/uk/kbackup/mainwindow.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kbackup/4778e718b2212917a612ca048ce876fb95dfa04e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kbackup.1
/usr/share/man/de/man1/kbackup.1
/usr/share/man/es/man1/kbackup.1
/usr/share/man/it/man1/kbackup.1
/usr/share/man/man1/kbackup.1
/usr/share/man/nl/man1/kbackup.1
/usr/share/man/sv/man1/kbackup.1
/usr/share/man/uk/man1/kbackup.1

%files locales -f kbackup.lang
%defattr(-,root,root,-)

