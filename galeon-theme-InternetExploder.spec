Summary:	IE theme for Galeon
Summary(pl.UTF-8):	Motyw IE dla Galeona
Name:		galeon-theme-InternetExploder
Version:	0.1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.iceflow.net/themes/InternetExploder-theme.tar.gz
# Source0-md5:	b387cf3a665182f285395164cff71a5b
URL:		http://www.iceflow.net/themes/
Requires:	galeon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a button theme for the Galeon web browser. Cover all the bases
of the different pixmap resources to make it look like IE.

%description -l pl.UTF-8
Motyw nadający Galeonowi wygląd Internet Explorera.

%prep
%setup  -q -n InternetExploder

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/galeon/themes/InternetExploder

install * $RPM_BUILD_ROOT%{_datadir}/galeon/themes/InternetExploder

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/galeon/themes/InternetExploder
